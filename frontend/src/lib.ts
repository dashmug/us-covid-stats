const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;

export const dataEndpoint = `${BACKEND_URL}/data`;
export const dailyEndpoint = `${BACKEND_URL}/daily`;
export const weeklyEndpoint = `${BACKEND_URL}/weekly`;
export const monthlyEndpoint = `${BACKEND_URL}/monthly`;

export interface CaseData {
  date: string;
  cases: number;
  recoveries: number;
  deaths: number;
}

export const seriesColors = ["#209cee", "#23d160", "#ff3860"];

export const latest = (n: number) => (xs: CaseData[]) => xs.slice(-n);

export const monthName = (date: Date) =>
  date.toLocaleString("default", { month: "long" });
