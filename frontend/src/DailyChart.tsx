import React from "react";
import ReactApexChart from "react-apexcharts";
import { CaseData, CaseDataColumn, seriesColors } from "./settings";

interface DailyChartProps {
  data: CaseData[];
  column: CaseDataColumn;
  seriesName: string;
}

const DailyChart = ({ data, column, seriesName }: DailyChartProps) => {
  const series = [
    {
      name: seriesName,
      data: data.map(({ date, ...columns }) => [date, columns[column]]),
    },
  ];

  const options = {
    chart: {
      zoom: {
        enabled: false,
      },
    },
    colors: [seriesColors[column]],
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
      height={150}
    />
  );
};

export default DailyChart;
