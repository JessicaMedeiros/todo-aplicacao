import { Routes } from '@angular/router';
import { TarefaLista } from './view/tarefa-lista/tarefa-lista';
import { TarefaDetalhe } from './view/tarefa-detalhe/tarefa-detalhe';

export const routes: Routes = [
    { path: '', component: TarefaLista },
  { path: 'tarefas/:id', component: TarefaDetalhe },
];
