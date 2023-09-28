
import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";

export const api = createApi({
  baseQuery: fetchBaseQuery({ baseUrl: process.env.REACT_APP_BASE_URL }),
  reducerPath: "adminApi",
  tagTypes: [ "BalanceData"],  // Adjusted the tagTypes to match the data being fetched
  endpoints: (build) => ({
    getBalanceData: build.query({  // Renamed to getBalanceData to match the endpoint
      query: () => ({
        url: `fa-balance/`,
        method: "GET"
      }),
      providesTags: ["BalanceData"],
    }),
  }),
});

export const {
  useGetBalanceDataQuery,
} = api;
