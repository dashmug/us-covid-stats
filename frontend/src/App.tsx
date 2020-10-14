import React, { SetStateAction, useEffect, useState } from "react";
import CumulativeChart from "./components/CumulativeChart";
import Summary from "./components/Summary";
import {
  dailyEndpoint,
  dataEndpoint,
  latest,
  monthlyEndpoint,
  monthName,
  weeklyEndpoint,
} from "./lib";
import Footer from "./components/Footer";
import LatestDataSection from "./components/LatestDataSection";

const fetcher = (
  url: string,
  setter: (data: SetStateAction<never[]>) => void
) => async () => {
  const result = await fetch(url);
  const caseData = await result.json();
  setter(caseData);
};

const App = () => {
  const [data, setData] = useState([]);
  const [daily, setDaily] = useState([]);
  const [weekly, setWeekly] = useState([]);
  const [monthly, setMonthly] = useState([]);

  useEffect(() => {
    const fetchData = fetcher(dataEndpoint, setData);
    const fetchDaily = fetcher(dailyEndpoint, setDaily);
    const fetchWeekly = fetcher(weeklyEndpoint, setWeekly);
    const fetchMonthly = fetcher(monthlyEndpoint, setMonthly);

    fetchData();
    fetchDaily();
    fetchWeekly();
    fetchMonthly();
  }, []);

  return (
    <section className="section">
      <div className="container">
        <h1 className="title has-text-centered">US COVID-19 Daily Cases</h1>
        <Summary data={daily} />
        <h2 className="subtitle">Cases, Recoveries, and Deaths</h2>
        <CumulativeChart data={data} />
      </div>
      <div className="container">
        <LatestDataSection
          heading="Past 7 Days"
          data={daily}
          range={latest(7)}
        />
        <LatestDataSection
          heading="Past 8 Weeks"
          data={weekly}
          range={latest(8)}
          dateColumn="Week ending at"
        />
        <LatestDataSection
          heading="Past 6 Months"
          data={monthly}
          range={latest(6)}
          dateColumn="Month"
          dateFormatter={monthName}
        />
      </div>
      <Footer />
    </section>
  );
};

export default App;
