import { nanoid } from "nanoid";
import React from "react";
import { Index as DatePicker } from "../../components/DatePicker";
import { Dropdown } from "../../components/Dropdown/Dropdown";
import { MenuItem } from "../../components/Dropdown/MenuItem";
import getTeacher from "../../services/teachers/getTeacher";
import getTeachers from "../../services/teachers/getTeachers";
import getTeachersAgain from "../../services/teachers/getTeachersAgain";
import "./Main.css";

const Main = () => {
  const menuRef = React.useRef();

  // const [windows, setWindows] = React.useState(false);
  const [date, setDate] = React.useState();
  const [teachers, setTeachers] = React.useState([]);
  const [schedule, setSchedule] = React.useState([]);
  const [loadingTeachers, setLoadingTeachers] = React.useState(true);
  const [_, setLoadingTeacher] = React.useState(true);
  const [data, setData] = React.useState([
    {
      id: nanoid(),
      teachingStaff: "",
    },
  ]);

  React.useEffect(() => {
    getTeachers()
      .then((teachersData) => {
        setTeachers(teachersData);
        setLoadingTeachers(false);
      })
      .catch((error) => {
        console.debug(error);
        setLoadingTeachers(false);
      });
  }, []);

  // React.useEffect(() => {
  //   console.log('data')
  //   console.log(data)
  //   console.log('schedule')
  //   console.log(schedule)
  // }, [data, schedule])

  // При изменении даты в календаре обновляется расписание
  React.useEffect(() => {
    if (data.length !== 0 && data[0].teachingStaff !== "") {
      getTeachersAgainHandler()
    }
  }, [date])

  // При изменении даты в календаре обновляется расписание
  async function getTeachersAgainHandler() {
    try {
      const res = await getTeachersAgain(data, date ? date : new Date())

      setSchedule(res)
    } catch (error) {
      console.debug(error);
    }
  }

  // При изменении даты в календаре обновляется расписание
  async function addTeacherInSchedule(id, date, rowId) {
    try {
      const teacherData = await getTeacher(id, date);

      if (!teacherData) {
        return;
      }

      setSchedule((prev) => [
        ...prev.filter((value) => value.id !== rowId),
      ]);

      setSchedule((prev) => [
        ...prev,
        {
          lessons: [...teacherData],
          ...data.find((value) => value.teachingStaff.id === id),
          id: data.find((value) => value.teachingStaff.id === id).teachingStaff.id,
          rowId: data.find((value) => value.teachingStaff.id === id).id,
        },
      ]);

      setLoadingTeacher(false);
    } catch (error) {
      setLoadingTeacher(false);
    }
  }

  // удаляет строку из расписания и из data
  function deleteRowHandler(rowId) {
    setSchedule((prev) => [...prev.filter((value) => { return value.rowId !== rowId })])
    setData(data.filter((value) => value.id !== rowId));
  }

  // При изменении дропдауна учитель добавляется в расписание или меняется на нового
  function handleTeachingStaffChange(value, rowId) {
    setSchedule((prev) => [...prev.filter((value) => { return value.rowId !== rowId })])
    setData((prevData) =>
      prevData.map((row) => {
        row.id === rowId
          ? addTeacherInSchedule(
            row.teachingStaff.id,
            new Date(date ? date : new Date()),
            row.id
          )
          : null;

        return row.id === rowId ? { ...row, teachingStaff: value } : row;
      })
    );
  }

  // при нажатии на кнопку "Добавить" добавляется новая строка
  function addRowHandler() {
    let newData = {
      id: nanoid(),
      teachingStaff: '',
    };

    setData([...data, newData]);
  }

  // если в колонке нет текста, то возвращает true
  function isColumnEmpty(columnNumber) {
    let isEmpty = true;

    if (schedule.length === 0) {
      return isEmpty;
    }

    for (const item of schedule) {
      const lessonsInColumn = item.lessons.filter(
        (lesson) => lesson.number === `${columnNumber} пара`
      );

      if (lessonsInColumn.length > 0) {
        isEmpty = false;
        break;
      }
    }

    return isEmpty;
  }

  return (
    <>
      <main className="main">
        {Array.isArray(data) &&
          data.map((row) => {
            return (
              <div className="row" key={row.id}>
                <Dropdown
                  label="ИМИТ"
                  className="faculty dropdown"
                  isEnable={false}
                ></Dropdown>
                <Dropdown
                  label="ПОВТАС"
                  className="department dropdown"
                  isEnable={false}
                ></Dropdown>
                <Dropdown
                  label="Пед. раб."
                  onChange={(value) => {
                    handleTeachingStaffChange(value, row.id);
                  }}
                  className="teaching-staff dropdown"
                  isEnable={true}
                  value={row.teachingStaff}
                >
                  {loadingTeachers ? (
                    <MenuItem>Loading...</MenuItem>
                  ) : (
                    teachers.map((item) => (
                      <MenuItem
                        ref={menuRef}
                        key={nanoid()}
                        value={item}
                        active={false}
                      >
                        {item.name}
                      </MenuItem>
                    ))
                  )}
                </Dropdown>
                {row.id === data[0].id ? null : (
                  <div className="delete-row">
                    <button
                      className="delete-row__button"
                      onClick={() => {
                        deleteRowHandler(row.id);
                      }}
                    >X
                    </button>
                  </div>
                )}
              </div>
            );
          })}
        <div className="utils">
          <button onClick={addRowHandler} className="utils__button">
            Добавить
          </button>
        </div>
        <DatePicker date={date} setDate={setDate} />
        <div className="table-container">
          <table className="table">
            <thead>
              <tr>
                <th>Пед. раб.</th>
                <th>
                  <p>Пара 1</p>
                  <p>08:00-09:30</p>
                </th>
                <th>
                  <p>Пара 2</p>
                  <p>09:40-11:10</p>
                </th>
                <th>
                  <p>Пара 3</p>
                  <p>11:20-12:50</p>
                </th>
                <th>
                  <p>Пара 4</p>
                  <p>13:20-14:50</p>
                </th>
                <th>
                  <p>Пара 5</p>
                  <p>15:00-16:30</p>
                </th>
                <th>
                  <p>Пара 6</p>
                  <p>16:40-18:10</p>
                </th>
                <th>
                  <p>Пара 7</p>
                  <p>18:20-19:50</p>
                </th>
                <th>
                  <p>Пара 8</p>
                  <p>20:00-21:30</p>
                </th>
              </tr>
            </thead>
            <tbody>
              {schedule.map && schedule.map((item) => (
                <tr key={item.rowId}>
                  <td className="teaching-staff">{item.teachingStaff.name}</td>
                  <td className={isColumnEmpty(1) ? 'empty' : null}>
                    {item.lessons.map((lesson) => {
                      return lesson.number === "1 пара" ? (
                        <div key={nanoid()}>
                          <span>{lesson.name}</span>
                          <p>Ауд.:{lesson.aud}</p>
                          <p>Группы: {lesson.groups.join('\n')}</p>
                        </div>
                      ) : null;
                    })}
                  </td>
                  <td className={isColumnEmpty(2) ? 'empty' : null}>
                    {item.lessons.map((lesson) => {
                      return lesson.number === "2 пара" ? (
                        <div key={nanoid()}>
                          <span>{lesson.name}</span>
                          <p>Ауд.:{lesson.aud}</p>
                          <p>Группы: {lesson.groups.join('\n')}</p>
                        </div>
                      ) : null;
                    })}
                  </td>
                  <td className={isColumnEmpty(3) ? 'empty' : null}>
                    {item.lessons.map((lesson) => {
                      return lesson.number === "3 пара" ? (
                        <div key={nanoid()}>
                          <span>{lesson.name}</span>
                          <p>Ауд.:{lesson.aud}</p>
                          <p>Группы: {lesson.groups.join('\n')}</p>
                        </div>
                      ) : null;
                    })}
                  </td>
                  <td className={isColumnEmpty(4) ? 'empty' : null}>
                    {item.lessons.map((lesson) => {
                      return lesson.number === "4 пара" ? (
                        <div key={nanoid()}>
                          <span>{lesson.name}</span>
                          <p>Ауд.:{lesson.aud}</p>
                          <p>Группы: {lesson.groups.join('\n')}</p>
                        </div>
                      ) : null;
                    })}
                  </td>
                  <td className={isColumnEmpty(5) ? 'empty' : null}>
                    {item.lessons.map((lesson) => {
                      return lesson.number === "5 пара" ? (
                        <div key={nanoid()}>
                          <span>{lesson.name}</span>
                          <p>Ауд.:{lesson.aud}</p>
                          <p>Группы: {lesson.groups.join('\n')}</p>
                        </div>
                      ) : null;
                    })}
                  </td>
                  <td className={isColumnEmpty(6) ? 'empty' : null}>
                    {item.lessons.map((lesson) => {
                      return lesson.number === "6 пара" ? (
                        <div key={nanoid()}>
                          <p>{lesson.name}</p>
                          <p>Ауд.:{lesson.aud}</p>
                          <p>Группы: {lesson.groups.join('\n')}</p>
                        </div>
                      ) : null;
                    })}
                  </td>
                  <td className={isColumnEmpty(7) ? 'empty' : null}>
                    {item.lessons.map((lesson) => {
                      return lesson.number === "7 пара" ? (
                        <div key={nanoid()}>
                          <span>{lesson.name}</span>
                          <p>Ауд.:{lesson.aud}</p>
                          <p>Группы: {lesson.groups.join('\n')}</p>
                        </div>
                      ) : null;
                    })}
                  </td>
                  <td className={isColumnEmpty(8) ? 'empty' : null}>
                    {item.lessons.map((lesson) => {
                      return lesson.number === "8 пара" ? (
                        <div key={nanoid()}>
                          <span>{lesson.name}</span>
                          <p>Ауд.:{lesson.aud}</p>
                          <p>Группы: {lesson.groups.join('\n')}</p>
                        </div>
                      ) : null;
                    })}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </main >
    </>
  );
};

export default Main;
