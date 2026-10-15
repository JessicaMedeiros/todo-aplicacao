// tarefa-lista/tarefa-lista.ts
import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { RouterLink } from '@angular/router';
import { MatListModule } from '@angular/material/list';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { MatChipsModule } from '@angular/material/chips';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { TarefaService } from '../../service/tarefa';
import { Tarefa } from '../../model/tarefa';

@Component({
  selector: 'app-tarefa-lista',
  standalone: true,
  imports: [
    CommonModule, FormsModule, RouterLink,
    MatListModule, MatButtonModule, MatIconModule, MatChipsModule,
    MatFormFieldModule, MatInputModule,
  ],
  templateUrl: './tarefa-lista.html',
})
export class TarefaLista implements OnInit {
  private tarefaService = inject(TarefaService);

  tarefas: Tarefa[] = [];
  novoTitulo = '';
  novaPrioridade = 0; 
  novaObs = '';

  ngOnInit() {
    this.carregar();
  }

  carregar() {
    this.tarefaService.listar().subscribe(tarefas => this.tarefas = tarefas);
  }

  adicionar() {
    if (!this.novoTitulo.trim()) return;
    this.tarefaService.criar({ titulo: this.novoTitulo, prioridade: this.novaPrioridade, observacao: this.novaObs })
    .subscribe(() => {
      this.novoTitulo = '';
      this.carregar();
    });
  }

  concluir(id: number, event: Event) {
    event.stopPropagation(); // impede de navegar pro detalhe ao clicar no botão
    this.tarefaService.concluir(id).subscribe(() => this.carregar());
  }

  remover(id: number, event: Event) {
    event.stopPropagation();
    this.tarefaService.deletar(id).subscribe(() => this.carregar());
  }
}