const LIMITE_TEXTO = 10;
const SUBSTITUICOES_REMOCAO_ACENTOS = {
  Á: "A",
  À: "A",
  Ã: "A",
  Â: "A",
  É: "E",
  Ê: "E",
  Í: "I",
  Ó: "O",
  Ô: "O",
  Õ: "O",
  Ú: "U",
  Ç: "C",
};
const SUBSTITUICOES_ADICAO_ACENTOS = {
  OLIVIA: "OLÍVIA",
  CECILIA: "CECÍLIA",
  MARCIA: "MÁRCIA",
  HELOISA: "HELOÍSA",
  JOSE: "JOSÉ",
  MAMAE: "MAMÃE",
  "MAÇA": "MAÇÃ",
  SAO: "SÃO",
  NAO: "NÃO",
  AGUA: "ÁGUA",
  ARVORE: "ÁRVORE",
  AVIAO: "AVIÃO",
  AVO: "AVÔ",
  BOTAO: "BOTÃO",
  BEBE: "BEBÊ",
  CARIE: "CÁRIE",
  CHA: "CHÁ",
  CEU: "CÉU",
  CORACAO: "CORAÇÃO",
  FACIL: "FÁCIL",
  FOSFORO: "FÓSFORO",
  LAPIS: "LÁPIS",
  MACA: "MAÇÃ",
  MAO: "MÃO",
  IRMAO: "IRMÃO",
  IRMA: "IRMÃ",
  PE: "PÉ",
  PAO: "PÃO",
  PESSEGO: "PÊSSEGO",
  RAPIDO: "RÁPIDO",
  SABADO: "SÁBADO",
  TENIS: "TÊNIS",
  VOVO: "VOVÓ",
  VOCE: "VOCÊ",
  MUSICA: "MÚSICA",
  HISTORIA: "HISTÓRIA",
  MAGICO: "MÁGICO",
  AGUIA: "ÁGUIA",
  ONIBUS: "ÔNIBUS",
  TELEVISAO: "TELEVISÃO",
  BALAO: "BALÃO",
  ALGODAO: "ALGODÃO",
  TUNEL: "TÚNEL",
  LEAO: "LEÃO",
  PO: "PÓ",
  NATACAO: "NATAÇÃO",
  ABOBORA: "ABÓBORA",
  ANAO: "ANÃO",
  CAMALEAO: "CAMALEÃO",
  ESCORPIAO: "ESCORPIÃO",
  ESPIAO: "ESPIÃO",
  AVIAOZINHO: "AVIÃOZINHO",
  DEDAO: "DEDÃO",
  CHAO: "CHÃO",
  VIOLAO: "VIOLÃO",
  BOLAOZINHO: "BALÃOZINHO",
  CANCAO: "CANÇÃO",
  DRAGAO: "DRAGÃO",
  FOGAO: "FOGÃO",
  LEAOZINHO: "LEÃOZINHO",
  MAOZINHA: "MÃOZINHA",
  FAISCA: "FAÍSCA",
  RACAO: "RAÇÃO",
  PRESEPIO: "PRESÉPIO",
  PONEI: "PÔNEI",
  INDIO: "ÍNDIO",
  XICARA: "XÍCARA",
  PURE: "PURÊ",
  IMA: "ÍMÃ",
  SANSAO: "SANSÃO",
  MONICA: "MÔNICA",
  CASCAO: "CASCÃO",
};

const elementos = {
  texto: document.querySelector("#texto"),
  entrada: document.querySelector("#entrada"),
  status: document.querySelector("#status"),
  ativarSom: document.querySelector("#ativar-som"),
  repetir: document.querySelector("#repetir"),
  limpar: document.querySelector("#limpar"),
};

const estado = {
  textoAtual: "",
  contextoAudio: null,
  origemAtual: null,
  desbloqueado: false,
  controladorFetch: null,
  tokenExecucao: 0,
};

function removerAcentos(texto) {
  let resultado = texto;
  for (const [acento, letra] of Object.entries(SUBSTITUICOES_REMOCAO_ACENTOS)) {
    resultado = resultado.replaceAll(acento, letra);
  }
  return resultado;
}

function adicionarAcentos(texto) {
  return SUBSTITUICOES_ADICAO_ACENTOS[texto] ?? texto;
}

function caractereEhLetra(caractere) {
  if (caractere.length !== 1) {
    return false;
  }
  const maiusculo = caractere.toUpperCase();
  const semAcentos = removerAcentos(maiusculo);
  return maiusculo === "Ç" || (semAcentos >= "A" && semAcentos <= "Z");
}

function normalizarCaractereLetra(caractere) {
  const maiusculo = caractere.toUpperCase();
  if (maiusculo === "Ç") {
    return "Ç";
  }
  return removerAcentos(maiusculo);
}

function transformarEntrada(texto) {
  let resultado = "";

  for (const caractere of texto) {
    if (resultado.length >= LIMITE_TEXTO) {
      break;
    }

    if (caractere >= "0" && caractere <= "9") {
      if (!resultado || /^\d+$/.test(resultado)) {
        resultado += caractere;
      }
      continue;
    }

    if (caractereEhLetra(caractere)) {
      if (!resultado || /^\D+$/u.test(resultado)) {
        resultado += normalizarCaractereLetra(caractere);
        resultado = adicionarAcentos(resultado);
      }
    }
  }

  return resultado;
}

function atualizarTela() {
  elementos.texto.textContent = estado.textoAtual;
}

function definirStatus(texto) {
  elementos.status.textContent = texto;
}

function pararAudioAtual() {
  if (estado.origemAtual) {
    estado.origemAtual.stop();
    estado.origemAtual.disconnect();
    estado.origemAtual = null;
  }
}

async function garantirAudioLiberado() {
  const ClasseAudioContext = window.AudioContext || window.webkitAudioContext;
  if (!estado.contextoAudio) {
    estado.contextoAudio = new ClasseAudioContext();
  }
  if (estado.contextoAudio.state !== "running") {
    await estado.contextoAudio.resume();
  }
  estado.desbloqueado = true;
  elementos.ativarSom.disabled = true;
  definirStatus("Som liberado.");
}

async function tocarTexto(texto) {
  if (!estado.desbloqueado || !texto) {
    return;
  }

  estado.tokenExecucao += 1;
  const tokenAtual = estado.tokenExecucao;

  if (estado.controladorFetch) {
    estado.controladorFetch.abort();
  }
  estado.controladorFetch = new AbortController();
  pararAudioAtual();

  try {
    const resposta = await fetch(`/api/audio/${encodeURIComponent(texto)}`, {
      signal: estado.controladorFetch.signal,
    });
    if (!resposta.ok) {
      throw new Error("Falha ao gerar áudio.");
    }

    const buffer = await resposta.arrayBuffer();
    if (tokenAtual !== estado.tokenExecucao) {
      return;
    }

    const audioBuffer = await estado.contextoAudio.decodeAudioData(buffer.slice(0));
    if (tokenAtual !== estado.tokenExecucao) {
      return;
    }

    const origem = estado.contextoAudio.createBufferSource();
    origem.buffer = audioBuffer;
    origem.connect(estado.contextoAudio.destination);
    origem.start(0);
    origem.onended = () => {
      if (estado.origemAtual === origem) {
        estado.origemAtual = null;
      }
    };
    estado.origemAtual = origem;
    definirStatus(`Tocando ${texto}.`);
  } catch (erro) {
    if (erro.name === "AbortError") {
      return;
    }
    definirStatus("Não foi possível tocar o áudio.");
  }
}

function aplicarTexto(texto) {
  estado.textoAtual = texto;
  atualizarTela();

  if (!texto) {
    estado.tokenExecucao += 1;
    if (estado.controladorFetch) {
      estado.controladorFetch.abort();
    }
    pararAudioAtual();
    definirStatus(
      estado.desbloqueado
        ? "Digite letras ou números."
        : "Toque em “Ativar som” para liberar o áudio no celular.",
    );
    return;
  }

  if (!estado.desbloqueado) {
    definirStatus("Texto pronto. Toque em “Ativar som” para ouvir.");
    return;
  }

  tocarTexto(texto);
}

elementos.entrada.addEventListener("input", () => {
  const textoTransformado = transformarEntrada(elementos.entrada.value);
  if (elementos.entrada.value !== textoTransformado) {
    elementos.entrada.value = textoTransformado;
  }
  aplicarTexto(textoTransformado);
});

elementos.entrada.addEventListener("keydown", (evento) => {
  if (evento.key === "Enter") {
    evento.preventDefault();
    tocarTexto(estado.textoAtual);
  }
});

elementos.ativarSom.addEventListener("click", async () => {
  try {
    await garantirAudioLiberado();
    elementos.entrada.focus();
    if (estado.textoAtual) {
      tocarTexto(estado.textoAtual);
    }
  } catch (erro) {
    definirStatus("Não foi possível liberar o áudio.");
  }
});

elementos.repetir.addEventListener("click", () => {
  tocarTexto(estado.textoAtual);
});

elementos.limpar.addEventListener("click", () => {
  elementos.entrada.value = "";
  aplicarTexto("");
  elementos.entrada.focus();
});

atualizarTela();
