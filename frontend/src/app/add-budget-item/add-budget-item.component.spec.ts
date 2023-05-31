import { ComponentFixture, TestBed } from '@angular/core/testing';
import { FormsModule } from '@angular/forms'; // new import

import { AddBudgetItemComponent } from './add-budget-item.component';

describe('AddBudgetItemComponent', () => {
  let component: AddBudgetItemComponent;
  let fixture: ComponentFixture<AddBudgetItemComponent>;

  beforeEach(async () => { // changed to async
    await TestBed.configureTestingModule({
      imports: [FormsModule], // FormsModule added here
      declarations: [AddBudgetItemComponent]
    }).compileComponents(); // await added before this method

    fixture = TestBed.createComponent(AddBudgetItemComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
