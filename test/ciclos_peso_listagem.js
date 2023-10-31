const ciclo_peso = {
  1: { ciclo: 1, peso: 1 },
  2: { ciclo: 2, peso: 2 },
  3: { ciclo: 3, peso: 3 },
  4: { ciclo: 4, peso: 4 },
};

for (const chave in ciclo_peso) {
  if (ciclo_peso.hasOwnProperty(chave)) {
    const cicloData = ciclo_peso[chave];

    console.log(cicloData);
  }
}

ciclo_nota = {
  1: { id_ciclo: 1, valor: 6.5 },
  2: { id_ciclo: 1, valor: 8.5 },
  4: { id_ciclo: 1, valor: 7.5 },
  5: { id_ciclo: 1, valor: 9.5 },
};
