import React from "react";
import ReactApexChart from "react-apexcharts";

const Chart = ({ data }) => {
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
    title: {
      text: "Cases, Recoveries, Deaths",
      align: "left",
    },
    colors: ["#008FFB", "#00E396", "#FF4560"],
    yaxis: {
      labels: {
        formatter: (val) => val.toLocaleString(),
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
        formatter: (val) => val.toLocaleString(),
      },
    },
  };
  return (
    <ReactApexChart
      options={options}
      series={series}
      type="line"
      height={450}
    />
  );
};

export default Chart;
