import logo from './logo.svg';
import './App.css';
import {BrowserRouter as Router, Route, Routes, Link} from 'react-router-dom';
import {DataGrid, GridColDef, GridValueGetterParams} from '@mui/x-data-grid';
import React, {useState, useEffect} from 'react';
import axios from 'axios';

import {Input} from "@mui/material";

function Projects() {

    const columns: GridColDef[] = [
        {field: 'id'},
        {field: 'WTG_numbers'},
        {field: 'total_kW'},
        {field: 'months_acquired'},
        {field: 'project_name'},
        {field: 'project_number'},
        {field: 'acquisition_date'},
        {field: 'number_3l_code'},
        {field: 'project_deal_type_id'},
        {field: 'project_group_id'},
        {field: 'project_status_id'},
        {field: 'company'},
    ];

    const loadData = async () => {
        const response = await axios.get('http://localhost:8000/projects/');
        setRows(response.data);
        setSearchedRows(response.data);

    };

    useEffect(() => {
        loadData();
    }, []);

    const [searchedRows, setSearchedRows] = useState([]);
    const [rows, setRows] = useState([]);
    const [searchTerm, setSearchTerm] = useState([]);

    const handleSearch = (event) => {
        let tempRows = [];
        for (const row of rows) {
            for (const v of Object.values(row)) {
                if (v && v.toString().toLowerCase().includes(event.target.value.toLowerCase())) {
                    tempRows.push(row);
                    break;
                }
            }
        }
        setSearchTerm(event.target.value)
        setSearchedRows(tempRows);
    };

    return (
        <div>
            <Input
                placeholder="Search"
                value={searchTerm}
                onChange={handleSearch}
            />
            <div style={{height: 800, width: '100%'}}>
                <DataGrid
                    rows={searchedRows}
                    columns={columns}
                />
            </div>
        </div>
    );
}

function App() {
    return (
        <Router>
            <Routes>
                <Route path="/projects/" element={<Projects/>}/>
            </Routes>
        </Router>
    );
}

export default App;
