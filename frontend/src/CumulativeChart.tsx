import React from "react";
import ReactApexChart from "react-apexcharts";
import { CaseData } from "./lib";

const CumulativeChart = ({ data }: { data: CaseData[] }) => {
  const series = [
    {
      name: "Total Cases",
      data: data.map(({ date, cases }) => [date, cases]),
    },
    {
      name: "Recoveries",
      data: data.map(({ date, recoveries }) => [date, recoveries]),
    },
    {
      name: "Deaths",
      data: data.map(({ date, deaths }) => [date, deaths]),
    },
  ];

  const options = {
    chart: {
      height: 450,
      zoom: {
        enabled: false,
      },
    },
    colors: ["#008FFB", "#00E396", "#FF4560"],
    yaxis: {
      labels: {
        formatter: (val: number) => val.toLocaleString(),
        minWidth: 100,
      },
      title: {
        text: "Cases",
      },
    },
    xaxis: {
      type: "datetime",
    },
    tooltip: {
      y: {
        formatter: (val: number) => val.toLocaleString(),
      },
    },
  };
  return (
    <ReactApexChart
      options={options}
      series={series}
      type="line"
      height={400}
    />
  );
};

export default CumulativeChart;
