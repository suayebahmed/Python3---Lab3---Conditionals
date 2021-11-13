# Federal Income Tax Calculator

# Taking user input for 2020 income
income = float(input("What was your 2020 income? "))

bracket_1 = 9875 * 0.1
bracket_2 = (40125 - 9875) * 0.12
bracket_3 = (85525 - 40125) * .22
bracket_4 = (163300 - 85525) * .24
bracket_5 = (207350 - 163300) * .32
bracket_6 = (518400 - 207350) * .35

if income <= 9875:
    tax_owed = income * 0.1
    eff_tax_rate = (tax_owed / income) * 100
    print(f"    First $ 9875:     $    {tax_owed:.2f}\n")
    print(f"Total Tax Owed:       $    {tax_owed:.2f}")
    print(f"Effective tax rate:   $      {eff_tax_rate:.1f}%")
elif income <= 40125:
    # bracket_1 = 9875 * 0.1
    bracket_2 = (income - 9875) * 0.12
    tax_owed = bracket_1 + bracket_2
    eff_tax_rate = (tax_owed / income) * 100
    print(f"    First $  9875:     $     {bracket_1:.2f}")
    print(f"$ 9875 -  $ 40125:     $    {bracket_2:.2f}\n")
    print(f"Total Tax Owed:        $    {tax_owed:.2f}")
    print(f"Effective tax rate:    $      {eff_tax_rate:.1f}%")
elif income <= 85525:
    # bracket_1 = 9875 * 0.1
    # bracket_2 = (40125 - 9875) * 0.12
    bracket_3 = (income - 40125) * .22
    tax_owed = bracket_1 + bracket_2 + bracket_3
    eff_tax_rate = (tax_owed / income) * 100
    print(f"    First $  9875:     $     {bracket_1:.2f}")
    print(f"$  9875 - $ 40125:     $    {bracket_2:.2f}")
    print(f"$ 40125 - $ 85525:     $    {bracket_3:.2f}\n")
    print(f"Total Tax Owed:        $   {tax_owed:.2f}")
    print(f"Effective tax rate:    $      {eff_tax_rate:.1f}%")
elif income <= 163300:
    # bracket_1 = 9875 *  0.1
    # bracket_2 = (40125 - 9875) * 0.12
    # bracket_3 = (85525 - 40125) * .22
    bracket_4 = (income - 85525) * .24
    tax_owed = bracket_1 + bracket_2 + bracket_3 + bracket_4
    eff_tax_rate = (tax_owed / income) * 100
    print(f"    First $   9875:    $     {bracket_1:.2f}")
    print(f"$  9875 - $  40125:    $    {bracket_2:.2f}")
    print(f"$ 40125 - $  85525:    $    {bracket_3:.2f}")
    print(f"$ 85525 - $ 163300:    $    {bracket_4:.2f}\n")
    print(f"Total Tax Owed:        $   {tax_owed:.2f}")
    print(f"Effective tax rate:    $      {eff_tax_rate:.1f}%")
elif income <= 207350:
    # bracket_1 = 9875 * 0.1
    # bracket_2 = (40125 - 9875) * 0.12
    # bracket_3 = (85525 - 40125) * .22
    # bracket_4 = (163300 - 85525) * .24
    bracket_5 = (income - 163300) * .32
    tax_owed = bracket_1 + bracket_2 + bracket_3 + bracket_4 + bracket_5
    eff_tax_rate = (tax_owed / income) * 100
    print(f"     First  $   9875:     $      {bracket_1:.2f}")
    print(f"$   9875 -  $  40125:     $     {bracket_2:.2f}")
    print(f"$  40125 -  $  85525:     $     {bracket_3:.2f}")
    print(f"$  85525 -  $ 163300:     $    {bracket_4:.2f}")
    print(f"$ 163300 -  $ 207350:     $    {bracket_5:.2f}\n")
    print(f"Total Tax Owed:           $    {tax_owed:.2f}")
    print(f"Effective tax rate:       $       {eff_tax_rate:.1f}%")
elif income <= 518400:
    # bracket_1 = 9875 * 0.1
    # bracket_2 = (40125 - 9875) * 0.12
    # bracket_3 = (85525 - 40125) * .22
    # bracket_4 = (163300 - 85525) * .24
    # bracket_5 = (207350 - 163300) * .32
    bracket_6 = (income - 207350) * .35
    tax_owed = bracket_1 + bracket_2 + bracket_3 + bracket_4 + bracket_5 + bracket_6
    eff_tax_rate = (tax_owed / income) * 100
    print(f"    First  $   9875:    $       {bracket_1:.2f}")
    print(f"$   9875 - $  40125:    $      {bracket_2:.2f}")
    print(f"$  40125 - $  85525:    $      {bracket_3:.2f}")
    print(f"$  85525 - $ 163300:    $     {bracket_4:.2f}")
    print(f"$ 163300 - $ 207350:    $     {bracket_5:.2f}")
    print(f"$ 207350 - $ 518400:    $    {bracket_6:.2f}\n")
    print(f"Total Tax Owed:         $    {tax_owed:.2f}")
    print(f"Effective tax rate:     $        {eff_tax_rate:.1f}%")
else:
    # bracket_1 = 9875 * 0.1
    # bracket_2 = (40125 - 9875) * 0.12
    # bracket_3 = (85525 - 40125) * .22
    # bracket_4 = (163300 - 85525) * .24
    # bracket_5 = (207350 - 163300) * .32
    # bracket_6 = (518400 - 207350) * .35
    bracket_7 = (income - 518400) * .37
    tax_owed = bracket_1 + bracket_2 + bracket_3 + bracket_4 + bracket_5 + bracket_6 + bracket_7
    eff_tax_rate = (tax_owed / income) * 100
    print(f"    First    $   9875:    $       {bracket_1:.2f}")
    print(f"$   9875  -  $  40125:    $      {bracket_2:.2f}")
    print(f"$  40125  -  $  85525:    $      {bracket_3:.2f}")
    print(f"$  85525  -  $ 163300:    $     {bracket_4:.2f}")
    print(f"$ 163300  -  $ 207350:    $     {bracket_5:.2f}")
    print(f"$ 207350  -  $ 518400:    $    {bracket_6:.2f}")
    print(f"$ 518400  -  $ {income}   $    {bracket_6:.2f}\n")
    print(f"Total Tax Owed:           $    {tax_owed:.2f}")
    print(f"Effective tax rate:       $        {eff_tax_rate:.1f}%")