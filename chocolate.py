def chocolate(money, price, wrappers_needed):
    """
    Takes int inputs of money, price, and number of wrappers needed to redeem another chocolate
    """
    our_wrappers = money / price

    redeemed = redeem_wrappers(our_wrappers, wrappers_needed)

def redeem_wrappers(wrappers_had, wrappers_needed):
    # base case: we have fewer wrappers than the redemption value
    if our_wrappers < wrappers_needed:
        redeemed = 0
    # recursive step: we have more wrappers needed than the redemption value
    elif our_wrappers >= wrappers_needed:  


chocolate(15, 1, 3)