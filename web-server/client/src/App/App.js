import 'materialize-css/dist/css/materialize.min.css'

import React from 'react'
import './App.css';
import StockPanel from '../StockPanel/StockPanel';

class App extends React.Component{
    render(){
        return (
            <div>
                {/* <img className='log' src = './logo.png' alt =''></img> */}
                <div className = 'container'>
                <StockPanel/>
                </div>    
            </div>
        );
    }
}

export default App;
