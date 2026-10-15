import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TarefaDetalhe } from './tarefa-detalhe';

describe('TarefaDetalhe', () => {
  let component: TarefaDetalhe;
  let fixture: ComponentFixture<TarefaDetalhe>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [TarefaDetalhe]
    })
    .compileComponents();

    fixture = TestBed.createComponent(TarefaDetalhe);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
