import React from "react";
// import DataChangerLeft from "./DataChangerLeft/DataChangerLeft";
// import DataChangerRight from "./DataChangerRight/DataChangerRight";
import DataPicker from "./DataPicker/DataPicker";
import "./index.css";
export const Index = ({ date, setDate }) => {
  return (
    <div className="datapicker-container">
      {/* <DataChangerLeft date={date} setDate={setDate} /> */}
      <DataPicker date={date} setDate={setDate} />
      {/* <DataChangerRight date={date} setDate={setDate} /> */}
    </div>
  );
};
