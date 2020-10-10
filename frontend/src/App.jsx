import React from "react";
import ChartFromAPI from "./ChartFromAPI";

const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;

const App = () => (
  <main className="wrapper">
    <section className="container">
      <h1>US COVID Daily Cases</h1>
      <ChartFromAPI url={`${BACKEND_URL}/data`} />
    </section>

    <footer className="footer">
      <section className="container">
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
      </section>
    </footer>
  </main>
);

export default App;
