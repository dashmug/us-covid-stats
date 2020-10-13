import TodayCard from "./TodayCard";
import React from "react";
import { CaseData } from "./lib";

const Summary = ({ data }: { data: CaseData[] }) => (
  <div className="columns">
    <div className="column">
      <TodayCard
        data={data}
        column="cases"
        backgroundClass="has-background-info-light"
      />
    </div>
    <div className="column">
      <TodayCard
        data={data}
        column="recoveries"
        backgroundClass="has-background-success-light"
      />
    </div>
    <div className="column">
      <TodayCard
        data={data}
        column="deaths"
        backgroundClass="has-background-danger-light"
      />
    </div>
  </div>
);

export default Summary;
