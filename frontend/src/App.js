import logo from './logo.svg';
import './App.css';
import {BrowserRouter as Router, Route, Routes, Link} from 'react-router-dom';


function Projects() {
    return (
        <div>
            <h1>Projects</h1>

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
