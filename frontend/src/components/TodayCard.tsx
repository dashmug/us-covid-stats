import React from "react";
import { CaseData } from "../lib";

interface TodayCardProps {
  data: CaseData[];
  column: Exclude<keyof CaseData, "date">;
  backgroundClass: string;
}

const TodayCard = ({ data, column, backgroundClass }: TodayCardProps) => {
  if (!data.length) {
    return (
      <div className={`card has-text-centered ${backgroundClass}`}>
        <div className="card-content">
          <p className="title is-4 has-text-info-dark">Loading...</p>
          <p className="subtitle is-6 has-text-info-dark">Loading...</p>
        </div>
      </div>
    );
  }

  const [previous, latest] = data.slice(-2);
  const latestStat = latest[column];
  const previousStat = previous[column];
  const difference = latestStat - previousStat;

  return (
    <div className={`card has-text-centered ${backgroundClass}`}>
      <div className="card-content">
        <p className="title is-4 has-text-info-dark">
          {latestStat.toLocaleString()} new cases
        </p>
        <p className="subtitle is-6 has-text-info-dark">
          {difference.toLocaleString()} from previous day
        </p>
      </div>
    </div>
  );
};

export default TodayCard;
