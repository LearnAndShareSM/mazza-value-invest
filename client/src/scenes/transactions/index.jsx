import React, { useState } from "react";
import { Box, useTheme } from "@mui/material";
import { DataGrid } from "@mui/x-data-grid";
import { useGetBalanceDataQuery } from 'state/api';
import Header from "components/Header";
import DataGridCustomToolbar from "components/DataGridCustomToolbar";

const Transactions = () => {
  const theme = useTheme();

  // values to be sent to the backend
  const [page, setPage] = useState(0);
  const [pageSize, setPageSize] = useState(20);
  const [sort, setSort] = useState({});
  const [search, setSearch] = useState("");

  const [searchInput, setSearchInput] = useState("");
  const { data, isLoading, error }  = useGetBalanceDataQuery({
    page,
    pageSize,
    sort: JSON.stringify(sort),
    search,
  });


  const columns = [
    {
      field: "fiscal_date_ending",
      headerName: "Fiscal Date Ending",
      flex: 1,
    },
    {
      field: "cik",
      headerName: "CIK",
      flex: 1,
    },
    {
      field: "ticker",
      headerName: "Ticker",
      flex: 1,
    },
    {
      field: "total_assets",
      headerName: "Total Assets",
      flex: 1,
    },
    {
      field: "total_liabilities",
      headerName: "Total Liabilities",
      flex: 1,
    },
  ];

  return (
    <Box m="1.5rem 2.5rem">
      <Header title="Transactions" subtitle="List of Transactions" />
      <Box
        height="80vh"
        sx={{
          "& .MuiDataGrid-root": {
            border: "none",
          },
          "& .MuiDataGrid-cell": {
            borderBottom: "none",
          },
          "& .MuiDataGrid-columnHeaders": {
            backgroundColor: theme.palette.primary.main,
            color: theme.palette.secondary[100],
            borderBottom: "none",
          },
          "& .MuiDataGrid-footerContainer": {
            backgroundColor: theme.palette.primary.light,
            color: theme.palette.secondary[100],
            borderTop: "none",
          },
          "& .MuiDataGrid-toolbarCointainer .MuiButton-text": {
            color: `${theme.palette.secondary[200]} !important`,
          },
        }}
      >
        <DataGrid
          loading={isLoading || !data}
          rows={data || []}
          getRowId={(row, index) => `${row.cik}-${index}-${row.fiscal_date_ending}`}
          columns={columns}
          rowCount={data && data.total || 0}
          rowsPerPageOptions={[20, 50, 100]}
          pagination
          page={page}
          pageSize={pageSize}
          paginationMode="server"
          sortingMode="server"
          onPageChange={(newPage) => setPage(newPage)}
          onPageSizeChange={(newPageSize) => setPageSize(newPageSize)}
          onSortModelChange={(newSortModel) => {
            console.log("New sort model:", newSortModel);
            setSort(newSortModel);
          }}
          slots={{
            toolbar: DataGridCustomToolbar,
          }}
          slotProps={{ toolbar: { searchInput, setSearchInput, setSearch } }}
        />
      </Box>
    </Box>
  );
};

export default Transactions;
