import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BudgetDisplayComponent } from './budget-display.component';

describe('BudgetDisplayComponent', () => {
  let component: BudgetDisplayComponent;
  let fixture: ComponentFixture<BudgetDisplayComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [BudgetDisplayComponent]
    });
    fixture = TestBed.createComponent(BudgetDisplayComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
