export default async function getTeachers() {
  let data;
  const url = "/api/teachers.json";

  try {
    await fetch(url)
      .then((response) => response.json())
      .then((json) => {
        data = json.teachers;
      })
      .catch((error) => {
        if (error) {
          console.error(error);
        }
      });

    return data;
  } catch (error) {
    console.debug(error);
  }
}
