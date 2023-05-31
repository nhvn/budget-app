import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BudgetListComponent } from './budget-list/budget-list.component';
import { BudgetItemComponent } from './budget-item/budget-item.component';
import { AddBudgetItemComponent } from './add-budget-item/add-budget-item.component';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';
import { BudgetDashboardComponent } from './budget-dashboard/budget-dashboard.component';
import { BudgetDisplayComponent } from './budget-dashboard/budget-display/budget-display.component';
import { ExpenseListComponent } from './budget-dashboard/expense-list/expense-list.component';
import { AddExpenseComponent } from './add-expense/add-expense.component';
import { EditExpenseComponent } from './edit-expense/edit-expense.component';

@NgModule({
  declarations: [
    AppComponent,
    BudgetListComponent,
    BudgetItemComponent,
    AddBudgetItemComponent,
    LoginComponent,
    RegisterComponent,
    BudgetDashboardComponent,
    BudgetDisplayComponent,
    ExpenseListComponent,
    AddExpenseComponent,
    EditExpenseComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
