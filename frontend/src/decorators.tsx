import React, { useEffect, useState } from "react";

export const withDataFromAPI = (url: string) => (BaseComponent: any) => () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const result = await fetch(url);
      const caseData = await result.json();
      setData(caseData);
    };

    fetchData();
  }, []);

  return <BaseComponent data={data} />;
};
