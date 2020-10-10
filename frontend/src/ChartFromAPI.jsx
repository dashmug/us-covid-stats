import React, { useEffect, useState } from "react";
import Chart from "./Chart";

const ChartFromAPI = ({ url }) => {
  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const result = await fetch(url);
      const caseData = await result.json();
      setData(caseData);
    };

    fetchData();
  }, [url]);

  return <Chart data={data} />;
};

export default ChartFromAPI;
