import React, { SetStateAction, useEffect, useState } from "react";
import CumulativeChart from "./CumulativeChart";
import DailyChart from "./DailyChart";
import Summary from "./Summary";
import MonthlyChart from "./MonthlyChart";
import WeeklyChart from "./WeeklyChart";

export const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;
const dataEndpoint = `${BACKEND_URL}/data`;
const dailyEndpoint = `${BACKEND_URL}/daily`;
const weeklyEndpoint = `${BACKEND_URL}/weekly`;
const monthlyEndpoint = `${BACKEND_URL}/monthly`;

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
        <h1 className="title has-text-centered">US COVID Daily Cases</h1>
        <Summary data={daily} />
        <h2 className="subtitle">Cases, Recoveries, and Deaths</h2>
        <CumulativeChart data={data} />
        <div className="columns">
          <div className="column is-one-third">
            <h2 className="subtitle">New Cases</h2>
            <DailyChart data={daily} column="cases" seriesName="Daily cases" />
            <WeeklyChart
              data={weekly}
              column="cases"
              seriesName="Weekly cases"
            />
            <MonthlyChart
              data={monthly}
              column="cases"
              seriesName="Monthly cases"
            />
          </div>
          <div className="column is-one-third">
            <h2 className="subtitle">Recoveries</h2>
            <DailyChart
              data={daily}
              column="recoveries"
              seriesName="Daily recoveries"
            />
            <WeeklyChart
              data={weekly}
              column="recoveries"
              seriesName="Weekly recoveries"
            />
            <MonthlyChart
              data={monthly}
              column="recoveries"
              seriesName="Monthly recoveries"
            />
          </div>
          <div className="column is-one-third">
            <h2 className="subtitle">Deaths</h2>
            <DailyChart
              data={daily}
              column="deaths"
              seriesName="Daily deaths"
            />
            <WeeklyChart
              data={weekly}
              column="deaths"
              seriesName="Weekly deaths"
            />
            <MonthlyChart
              data={monthly}
              column="deaths"
              seriesName="Monthly deaths"
            />
          </div>
        </div>

        {/*<div className="columns">*/}
        {/*  <div className="column">*/}
        {/*    <h2 className="subtitle">Total Cases</h2>*/}
        {/*    <DailyChart />*/}
        {/*  </div>*/}
        {/*  <div className="column">*/}
        {/*    <h2 className="subtitle">Recoveries</h2>*/}
        {/*    <WeeklyChart />*/}
        {/*  </div>*/}
        {/*  <div className="column">*/}
        {/*    <h2 className="subtitle">Deaths</h2>*/}
        {/*    <MonthlyChart />*/}
        {/*  </div>*/}
        {/*</div>*/}

        <footer className="footer">
          <div className="content has-text-centered">
            <p>
              This project is an entry for{" "}
              <a href="https://acloudguru.com/">A Cloud Guru</a>'s{" "}
              <a href="https://acloudguru.com/blog/news/introducing-the-cloudguruchallenge">
                #cloudguruchallenge
              </a>{" "}
              (
              <a href="https://acloudguru.com/blog/engineering/cloudguruchallenge-python-aws-etl">
                Event-Driven Python on AWS
              </a>
              ).
            </p>
          </div>
        </footer>
      </div>
    </section>
  );
};

export default App;
