// tarefa-detalhe/tarefa-detalhe.ts
import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ActivatedRoute, Router } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { MatCardModule } from '@angular/material/card';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';
import { TarefaService } from '../../service/tarefa';
import { Tarefa } from '../../model/tarefa';

@Component({
  selector: 'app-tarefa-detalhe',
  standalone: true,
  imports: [CommonModule, FormsModule, MatCardModule, MatFormFieldModule, MatInputModule, MatButtonModule],
  templateUrl: './tarefa-detalhe.html',
})
export class TarefaDetalhe implements OnInit {
  private route = inject(ActivatedRoute);
  private router = inject(Router);
  private tarefaService = inject(TarefaService);

  tarefa?: Tarefa;

  ngOnInit() {
    const id = Number(this.route.snapshot.paramMap.get('id'));
    this.tarefaService.buscarPorId(id).subscribe(tarefa => this.tarefa = tarefa);
  }

  salvar() {
    if (!this.tarefa) return;
    this.tarefaService.atualizar(this.tarefa.id, {
      titulo: this.tarefa.titulo,
      prioridade: this.tarefa.prioridade,
      observacao: this.tarefa.observacao,
    }).subscribe(() => this.router.navigate(['/']));
  }

  voltar() {
    this.router.navigate(['/']);
  }
}