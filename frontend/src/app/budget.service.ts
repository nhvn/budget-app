import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class BudgetService {

  private baseUrl = '/api/budget';  // Update this with your Django backend URL

  constructor(private http: HttpClient) { }

  fetchBudgetItems(): Observable<any[]> {
    return this.http.get<any[]>(`${this.baseUrl}/`);
  }

  createBudgetItem(item: any): Observable<any> {
    return this.http.post<any>(`${this.baseUrl}/`, item);
  }

  updateBudgetItem(item: any): Observable<any> {
    return this.http.put<any>(`${this.baseUrl}/${item.id}/`, item);
  }

  deleteBudgetItem(itemId: number): Observable<any> {
    return this.http.delete<any>(`${this.baseUrl}/${itemId}/`);
  }
}
