import React from "react";
import { CaseData } from "../lib";

interface TableProps {
  data: CaseData[];
  range: (xs: CaseData[]) => CaseData[];
  dateColumn?: string;
  dateFormatter?: (date: Date) => string;
}

const Table = ({
  data,
  range,
  dateColumn = "Day",
  dateFormatter = (date) => date.toLocaleDateString(),
}: TableProps) => {
  const mapper = (row: CaseData) => (
    <tr className="has-text-right">
      <td>{dateFormatter(new Date(row.date))}</td>
      <td className="has-text-info-dark">{row.cases}</td>
      <td className="has-text-success-dark">{row.recoveries}</td>
      <td className="has-text-danger-dark">{row.deaths}</td>
    </tr>
  );
  return (
    <div className="table-container">
      <table className="table is-bordered is-striped is-narrow is-hoverable is-fullwidth">
        <thead>
          <tr className="has-text-centered">
            <th>{dateColumn}</th>
            <th className="has-text-info-dark">New Cases</th>
            <th className="has-text-success-dark">New Recoveries</th>
            <th className="has-text-danger-dark">New Deaths</th>
          </tr>
        </thead>
        <tbody>{range(data).map(mapper)}</tbody>
      </table>
    </div>
  );
};

export default Table;
