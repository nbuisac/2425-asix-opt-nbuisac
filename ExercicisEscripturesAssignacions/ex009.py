quantitat = float(input("Entra una quantitat -> ")) * 100
## Anirem desglossant començant per bitllets, de 500 acabant amb monedes de 1ct
bitllets = quantitat // 50000
quantitat = quantitat % 50000
print(bitllets, "bitllets de 500")

bitllets = quantitat // 20000
quantitat = quantitat % 20000
print(bitllets, "bitllets de 200")

bitllets = quantitat // 10000
quantitat = quantitat % 10000
print(bitllets, "bitllets de 100")

bitllets = quantitat // 5000
quantitat = quantitat % 5000
print(bitllets, "bitllets de 50")

bitllets = quantitat // 2000
quantitat = quantitat % 2000
print(bitllets, "bitllets de 20")

bitllets = quantitat // 1000
quantitat = quantitat % 1000
print(bitllets, "bitllets de 10")

bitllets = quantitat // 500
quantitat = quantitat % 500
print(bitllets, "bitllets de 5")

monedes = quantitat // 200
quantitat = quantitat % 200
print(monedes, "monedes de 2 €")

monedes = quantitat // 100
quantitat = quantitat % 100
print(monedes, "monedes de 1 €")

monedes = quantitat // 50
quantitat = quantitat % 50
print(monedes, "monedes de 50 cts")

monedes = quantitat // 20
quantitat = quantitat % 20
print(monedes, "monedes de 20 cts")

monedes = quantitat // 10
quantitat = quantitat % 10
print(monedes, "monedes de 10 cts")

monedes = quantitat // 5
quantitat = quantitat % 5
print(monedes, "monedes de 5 cts")

monedes = quantitat // 2
quantitat = quantitat % 2
print(monedes, "monedes de 2 cts")

monedes = quantitat // 1
quantitat = quantitat % 1
print(monedes, "monedes de 1 cts")