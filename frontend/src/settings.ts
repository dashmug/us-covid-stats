export const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;

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
