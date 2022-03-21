#include <stdio.h>
#include <string.h>

int main(void) {
  FILE *fConv86;
  char buffer[1001];

  printf("Antes\n");

  fConv86 = fopen("/portaloptrib/TESHUVA/sparta/DEV/arquivos/clone2/ajuste_cadastral_clone2/portaloptrib/TESHUVA/sparta/PROD/entradas/conv86/SP/pleito_202011_versao_202011_escopo_2016_corrigido/202011EN_corrigido.txt", "r");

  if(!fConv86) {
     printf("Falha ao abrir o arquivo\n");
     return 1;
  }

  fseek(fConv86,0,SEEK_END);
  printf("Tam: %ld\n", ftell(fConv86));

  fseek(fConv86,0,SEEK_SET);

  while (fgets(buffer, 1000, fConv86)) {
    printf("%d\n", (int)strlen(buffer));
  }

  close(fConv86);

  printf("Depois\n");
  
  return 0;
}
