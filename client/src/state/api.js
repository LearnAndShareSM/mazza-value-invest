// import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";

// export const api = createApi({
//   baseQuery: fetchBaseQuery({ baseUrl: process.env.REACT_APP_BASE_URL }),
//   reducerPath: "adminApi",
//   tagTypes: ["User", " Transactions"],
//   endpoints: (build) => ({
//     getUser: build.query({
//       query: (id) => `general/user/${id}`,
//       providesTags: ["User"],
//     }),
//     getTransactions: build.query({
//       query: ({ page, pageSize, sort, search }) => ({
//         url: "client/transactions",
//         method: "GET",
//         params: { page, pageSize, sort, search },
//       }),
//       providesTags: ["Transactions"],
//     }),

//   }),
// });

// export const {
//   useGetUserQuery,
//   useGetTransactionsQuery,
// } = api;

import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";

export const api = createApi({
  baseQuery: fetchBaseQuery({ baseUrl: process.env.REACT_APP_BASE_URL }),
  reducerPath: "adminApi",
  tagTypes: ["BalanceOptions", "BalanceData"],  // Adjusted the tagTypes to match the data being fetched
  endpoints: (build) => ({
    getBalanceOptions: build.query({  // Renamed to getBalanceOptions to match the endpoint
      query: () => `fa-balance/options`,
      providesTags: ["BalanceOptions"],
    }),
    getBalanceData: build.query({  // Renamed to getBalanceData to match the endpoint
      query: ({ period, ticker }) => ({
        url: `fa-balance/`,
        method: "GET",
        params: { period, ticker },
      }),
      providesTags: ["BalanceData"],
    }),
  }),
});

export const {
  useGetBalanceOptionsQuery,
  useGetBalanceDataQuery,
} = api;
