import Algorithmia

input = {
  src: "Algorithmia is de enige plek waar je nederlands met syntaxnet kunnen ontleden.",
  format: "conll",
  language: "dutch"
}
client = Algorithmia.client('simMoh5s9nSbP+51LZ5dEA7Pejv1')
algo = client.algo('deeplearning/Parsey/1.0.4')
print algo.pipe(input)