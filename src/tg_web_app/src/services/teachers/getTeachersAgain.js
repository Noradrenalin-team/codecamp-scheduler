import getTeacher from "./getTeacher";

export default async function getTeachersAgain(array, date) {
  const teachers = await Promise.all(
    array.map(async (value) => {
      const response = await getTeacher(value.teachingStaff.id, date);
      return {
        lessons: [...response],
        teachingStaff: value.teachingStaff,
        id: value.teachingStaff.id,
        rowId: value.id,
      };
    })
  );

  return teachers;
}
