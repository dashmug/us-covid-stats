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

export type CaseDataColumn = Exclude<keyof CaseData, "date">;

export const seriesColors: Record<CaseDataColumn, string> = {
  cases: "#209cee",
  recoveries: "#23d160",
  deaths: "#ff3860",
};
