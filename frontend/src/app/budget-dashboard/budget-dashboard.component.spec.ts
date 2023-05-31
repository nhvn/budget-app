import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BudgetDashboardComponent } from './budget-dashboard.component';

describe('BudgetDashboardComponent', () => {
  let component: BudgetDashboardComponent;
  let fixture: ComponentFixture<BudgetDashboardComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [BudgetDashboardComponent]
    });
    fixture = TestBed.createComponent(BudgetDashboardComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
