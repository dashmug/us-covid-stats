import React from "react";
import ReactApexChart from "react-apexcharts";
import { CaseData, seriesColors } from "../lib";

interface ChartProps {
  data: CaseData[];
  range: (xs: CaseData[]) => CaseData[];
}

const Chart = ({ data, range }: ChartProps) => {
  const series = [
    {
      name: "New Cases",
      data: range(data).map(({ date, cases }) => [date, cases]),
    },
    {
      name: "New Recoveries",
      data: range(data).map(({ date, recoveries }) => [date, recoveries]),
    },
    {
      name: "New Deaths",
      data: range(data).map(({ date, deaths }) => [date, deaths]),
    },
  ];

  const options = {
    chart: {
      zoom: {
        enabled: false,
      },
    },
    colors: seriesColors,
    yaxis: {
      labels: {
        formatter: (val: number) => val.toLocaleString(),
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
      height={300}
    />
  );
};

export default Chart;
