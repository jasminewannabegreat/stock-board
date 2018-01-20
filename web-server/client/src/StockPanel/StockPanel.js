import './StockPanel.css';
import 'materialize-css/dist/css/materialize.min.css';
import 'materialize-css/dist/js/materialize.js';

import React from 'react';
import StockCard from '../StocksCard/StocksCard';

class StockPanel extends React.Component{
    constructor(){
        super();
        this.state = {stocks:null};
        this.handleScroll = this.handleScroll.bind(this);
    }

    componentDidMount() {
        this.loadMoreStocks();
        this.loadMoreStocks = _.debounce(this.loadMoreStocks, 1000);
        window.addEventListener('scroll', this.handleScroll);
    }

    handleScroll() {
        let scrollY = window.scrollY ||
                      window.pageYOffset ||
                      document.documentElement.scrollTop;
        if ((window.innerHeight + scrollY) >= (document.body.offsetHeight - 50)) {
            console.log('Loading more stocks');
            this.loadMoreNews();
        }
    }

    loadMoreStocks(){
        this.setState({
            stocks:[
                    {
                        'url':'',
                        'title':'AGTC',
                        'open': 4.7,
                        'price': 4.8,
                        'volume': 45239,
                        'trade_datetime': '2017-09-07 20:00:00 UTC+0000',
                        'reason':'recommand'
                    },
                    {
                        'url':'',
                        'title':'AGTC',
                        'open': 4.7,
                        'price': 4.8,
                        'volume': 45239,
                        'trade_datetime': '2017-09-07 20:00:00 UTC+0000',
                        'reason':'hot'
                    }
                ]
        });
        // let request = new Request('http://localhost:3000/stocks', {
        //     method: 'GET',
        //     cache: false
        // });
      
        // fetch(request)
        // .then((res) => res.json())
        // .then((news) => {
        //     this.setState({
        //         news:this.state.stocks ? this.state.stocks.concat(stocks) : stocks,
        //     });
        // });
    }

    renderStocks(){
        const stock_list = this.state.stocks.map(function(stocks){
            console.log(stocks);
            return(
                <a className = 'list-ground-item' href = "#">
                <StockCard stocks={stocks} />
                --------------------------------------------------
                </a>
            );
    
        });

        return(
            <div className='container-fluid'>
              <div className='list-group'>
                {stock_list}
              </div>
            </div>
        )
    }
    render() {
        if (this.state.stocks) {
          return(
            <div>
              {this.renderStocks()}
            </div>
          );
        } else {
          return(
            <div>
              <div id='app-loading'>
                Loading...
              </div>
            </div>
          );
        }
    }
}

export default StockPanel;