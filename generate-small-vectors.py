import json
import io
import qrcode
import qrcode.image.svg
ecc = {
    "low": qrcode.constants.ERROR_CORRECT_L,
    "medium": qrcode.constants.ERROR_CORRECT_M,
    "quartile": qrcode.constants.ERROR_CORRECT_Q,
    "high": qrcode.constants.ERROR_CORRECT_H,
}
res = []
emoji = ['#️⃣','🧜‍♂️','🏎','🔍','🔻']
for lvl in ecc:
    ecc = ecc[lvl]

    alphabets = ['0123456789', '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ $%*+-./:',  emoji]
    for a in alphabets:
        text = ''
        for i in range(0, 1000):
            text += a[(i) % len(a)]
            qr = qrcode.QRCode(error_correction=ecc[lvl])
            try:
                qr.add_data(text, 0)
                f = io.StringIO()
                qr.print_ascii(out=f, invert=True)
                f.seek(0)
                out = f.read()
                res.append({"text": "" + text, "ecc": lvl, "out": out})
            except Exception:
                break

with open('test_cases.json', 'w', encoding='utf8') as f:
    f.write(json.dumps(res))

print('T', len(res))

















