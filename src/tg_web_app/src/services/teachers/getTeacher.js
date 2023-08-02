import addZeros from "../../utils/addZeros/addZeros";

export default async function getTeacher(id, date) {
  const url = `/api/${id}.json`;
  let curDate = new Date(date);

  try {
    const response = await fetch(url);
    const json = await response.json();

    const data = json[
      `${addZeros(curDate.getDate())}.${addZeros(curDate.getMonth() + 1)}.${curDate.getFullYear()}`
    ];
    
    console.log(
      data
        ? data
        : `Not found\n> Please check date`
    );

    return data ? data : [];
  } catch (error) {
    console.debug(error);
    return null;
  }
}
