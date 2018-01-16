from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
  if request.method == 'POST':

    sent = request.form['sent']
    print('sentence: ', request.form['sent'])

    with open('sents/counter.txt', 'r') as f:
      no_of_sents = int(f.readline().strip())

    print('no of sents: ', no_of_sents, type(no_of_sents))

    with open('sents/counter.txt', 'w') as f:
      f.write(str(no_of_sents+1))

    with open('sents/{:04d}.txt'.format(no_of_sents), 'w') as f:
      f.write(sent)

    open('sents/{:04d}.ann'.format(no_of_sents), 'a').close()

    return render_template('index.html')
  return render_template('index.html')

if __name__ == '__main__':
    app.run(port=5001)