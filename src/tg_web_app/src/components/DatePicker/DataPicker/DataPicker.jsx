import React from "react";
import "./DataPicker.css";

const DataPicker = ({ date, setDate }) => {
  const handleDateTimeChange = (event) => {
    setDate(event.target.value);
  };

  return (
    <>
      <input
        type="date"
        value={date}
        onChange={(e) => {
          handleDateTimeChange(e);
        }}
      />
    </>
  );
};

export default DataPicker;
