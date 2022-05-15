<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">InsiderAI</h3>

  <p align="center">
    Predicting stock movements with insider trading data
    <br />
  </p>
</div>

<!-- ABOUT THE PROJECT -->

## About The Project

### How it works

The free finnhub API is used to download one year of insider trading data from all stocks currently listed on the S&P 500. Corresponding stock price data is then collected, representing future prices 1 day after the trade, 1 week after the trade, 2 weeks after the trade, and 1 month after the trade. Accordingly, we can try and establish a relationship between a given insider trade and the future stock price.

To do so, the h2o library is used. First, the collected data is separated into a training set and a test set. Second, a GBM model is created using various metrics from insider trades to try and predict whether a given stock will go up or down in price. Third, the model is trained using the training set and tested with the test set (the test results are then outputted to the `predictions` folder).

So you do not have to clone the project yourself, download all of the data, and train the models, I have included the dataset used for training in the `data` folder as well as the predicted price movements in the `predictions` folder.

### How to interpret the results

Example results are provided in the `predictions` folder.

In each CSV, there are 3 columns. The first column represents the actual outcome - i.e. whether the stock went up or down in price. Here, a "1" indicates that the stock went up in price and a "0" indicates that it went down. The following two columns represent the models confidence that the price will go up or down ("p0" = confidence price will go down, "p1" = confidence price will go up).

In essence, each row in the CSV corresponds to a single insider trade from the test data and represents the models confidence that the stock will go up or down in price in light of that insider trade.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- RUNNING LOCALLY -->

## Running locally

### Prerequisites

-   python3
-   Latest Java Runtime Environment

### Installation

1. Get a free API Key at [https://finnhub.io/](https://finnhub.io/)
2. Clone the repo
    ```sh
    git clone https://github.com/your_username_/Project-Name.git
    ```
3. Change to project directory
    ```sh
    cd InsiderAI
    ```
4. Install project dependencies
    ```sh
    pip3 install -r requirements.txt
    ```
5. Enter your finnhub API key in `main.py`
    ```python
    FH_API_KEY = 'YOUR_API_KEY_HERE'
    ```
6. Run the program!
    ```sh
    python3 main.py
    ```

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>
