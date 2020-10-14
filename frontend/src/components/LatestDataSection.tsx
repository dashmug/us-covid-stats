import Table from "./Table";
import { CaseData } from "../lib";
import Chart from "./Chart";
import React from "react";

interface LatestDataSectionProps {
  heading: string;
  data: CaseData[];
  range: (xs: CaseData[]) => CaseData[];
  dateColumn?: string;
  dateFormatter?: (date: Date) => string;
}

const LatestDataSection = ({
  heading,
  data,
  range,
  dateColumn,
  dateFormatter,
}: LatestDataSectionProps) => (
  <>
    <h2 className="subtitle">{heading}</h2>
    <div className="columns">
      <div className="column">
        <Table
          data={data}
          range={range}
          dateColumn={dateColumn}
          dateFormatter={dateFormatter}
        />
      </div>
      <div className="column">
        <Chart data={data} range={range} />
      </div>
    </div>
  </>
);

export default LatestDataSection;
