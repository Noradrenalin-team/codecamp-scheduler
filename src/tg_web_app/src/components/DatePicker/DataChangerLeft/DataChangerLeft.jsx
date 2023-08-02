import "./DataChangerLeft.css";

const DataChangerLeft = ({ setDate }) => {
  return (
    <button
      className="left"
      onClick={() => {
        setDate((prev) => {
          const date = new Date(prev);
          date.setDate(date.getDate() - 1);
          console.log(prev);
          console.log(date.toISOString().slice(0, 10));
          return date.toISOString().slice(0, 10);
        });
      }}
    >
      {"<"}
    </button>
  );
};

export default DataChangerLeft;
