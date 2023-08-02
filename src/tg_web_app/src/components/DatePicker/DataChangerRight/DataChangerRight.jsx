import "./DataChangerRight.css";

const DataChangerRight = ({ setDate }) => {
  return (
    <button
      className="right"
      onClick={() => {
        setDate((prev) => {
          const date = new Date(prev);
          date.setDate(date.getDate() + 1);
          console.log(prev);
          return date.toISOString().slice(0, 10);
        });
      }}
    >
      {">"}
    </button>
  );
};

export default DataChangerRight;
