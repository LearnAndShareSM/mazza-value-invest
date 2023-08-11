import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [data, setData] = useState([]);
  const [tickers, setTickers] = useState([]); // per memorizzare tutti i possibili ticker
  const [selectedTicker, setSelectedTicker] = useState(""); // per memorizzare il ticker selezionato

  useEffect(() => {
    // Supponendo che tu abbia un endpoint /available_tickers che restituisce tutti i ticker
    axios.get('http://localhost:8000/available_tickers/')
      .then(response => {
        setTickers(response.data);
      })
      .catch(error => {
        console.error('Error fetching tickers:', error);
      });
  }, []);

  useEffect(() => {
    let url = `http://localhost:8000/fa_balance/?`;
    if (selectedTicker) {
      url += `ticker=${selectedTicker}`;
    }

    axios.get(url)
      .then(response => {
        setData(response.data);
      })
      .catch(error => {
        if (error.response) {
          console.error('Data:', error.response.data);
          console.error('Status:', error.response.status);
          console.error('Headers:', error.response.headers);
        } else if (error.request) {
          console.error('No response:', error.request);
        } else {
          console.error('Error', error.message);
        }
      });

  }, [selectedTicker]);

  return (
    <div className="App">
      <h1>FA Balance</h1>
      <div>
        <label>Filter by Ticker:</label>
        <select value={selectedTicker} onChange={e => setSelectedTicker(e.target.value)}>
          <option value="">--Select a Ticker--</option>
          {tickers.map(ticker => (
            <option key={ticker} value={ticker}>{ticker}</option>
          ))}
        </select>
      </div>
      <div>
        {data.map(item => (
          <div key={item.cik}>  {/* Assumendo che 'cik' sia un campo univoco nella tua tabella */}
            Ticker: {item.ticker}, Cash: {item.cash_and_cash_equivalents}, Date: {item.fiscal_date_ending}
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
