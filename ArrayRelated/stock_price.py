# an efficient function that takes stock_prices and returns the best profit I could have made from any purchase
# and any sale.


class StockUtil:

    @staticmethod
    def get_max_profit(sale_rates):
        length = len(sale_rates)
        profit = 0

        for i in range(length):
            for j in range(i, length):
                current_profit = sale_rates[j] - sale_rates[i]
                if current_profit >= profit:
                    profit = current_profit

        return profit


    @staticmethod
    def get_max_profit_for_a_day(sale_rates):
        length = len(sale_rates)
        profit = 0

        for i in range(length-1):
            current_profit = sale_rates[i+1] - sale_rates[i]
            if current_profit >= profit:
                profit = current_profit

        return profit


if __name__ == '__main__':

    result = StockUtil.get_max_profit([12, 8, 9, 24, 67, 6])
    result = StockUtil.get_max_profit_for_a_day([12, 8, 9, 24, 67, 6])

    print(result)
