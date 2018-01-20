import React from 'react';

import './StockCard.css';

class StockCard extends React.Component{
    redirectToUrl(url) {
        window.open(url, '_blank');
    }

    render(){
        console.log(this.props.stocks.history != null);
        return(
            <div className="stocks-container" onClick={() => this.redirectToUrl(this.props.stocks.url)}>
                <div className='stock'>
                    <h4>{this.props.stocks.index}
                    </h4>
                    <div className='stockInfo'>
                        <div className='priceInfo'>   
                            Open: {this.props.stocks.open}
                            {'             '}
                            Price: {this.props.stocks.price} 
                            {'             '}
                            change: {this.props.stocks.change}
                            {'             '}
                            percent_change: {this.props.stocks.percent_change}
                            {'             '}
                            prev_close: {this.props.stocks.prev_close}  
                            {'             '}
                            Vol: {this.props.stocks.volume}                          
                        </div>
                    </div>
                </div>
            </div>
        );
    }
}

export default StockCard