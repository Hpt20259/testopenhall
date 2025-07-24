import React, { useState, useEffect, useCallback } from 'react';
import { Container, Typography, Box, Snackbar, Alert } from '@mui/material';
import './App.css';
import EquationForm from './components/EquationForm';
import EquationList from './components/EquationList';
import { Equation } from './types';
import { getEquations, createEquation, updateEquation, deleteEquation } from './services/api';

function App() {
  const [equations, setEquations] = useState<Equation[]>([]);
  const [editingEquation, setEditingEquation] = useState<Equation | null>(null);
  const [notification, setNotification] = useState<{ message: string; type: 'success' | 'error' } | null>(null);

  const showNotification = (message: string, type: 'success' | 'error') => {
    setNotification({ message, type });
  };

  const fetchEquations = useCallback(async () => {
    try {
      const data = await getEquations();
      setEquations(data);
    } catch (error) {
      console.error('Lỗi khi tải dữ liệu:', error);
      showNotification('Không thể tải dữ liệu phương trình', 'error');
    }
  }, []);

  useEffect(() => {
    fetchEquations();
  }, [fetchEquations]);

  const handleAddEquation = async (a: number, b: number, c: number) => {
    try {
      await createEquation({ a, b, c });
      fetchEquations();
      showNotification('Phương trình đã được thêm thành công', 'success');
    } catch (error) {
      console.error('Lỗi khi thêm phương trình:', error);
      showNotification('Không thể thêm phương trình', 'error');
    }
  };

  const handleUpdateEquation = async (a: number, b: number, c: number) => {
    if (!editingEquation || !editingEquation.id) return;
    
    try {
      await updateEquation(editingEquation.id, { a, b, c });
      setEditingEquation(null);
      fetchEquations();
      showNotification('Phương trình đã được cập nhật thành công', 'success');
    } catch (error) {
      console.error('Lỗi khi cập nhật phương trình:', error);
      showNotification('Không thể cập nhật phương trình', 'error');
    }
  };

  const handleDeleteEquation = async (id: number) => {
    try {
      await deleteEquation(id);
      fetchEquations();
      showNotification('Phương trình đã được xóa thành công', 'success');
    } catch (error) {
      console.error('Lỗi khi xóa phương trình:', error);
      showNotification('Không thể xóa phương trình', 'error');
    }
  };

  const handleEditEquation = (equation: Equation) => {
    setEditingEquation(equation);
  };

  const handleCloseNotification = () => {
    setNotification(null);
  };

  return (
    <Container maxWidth="lg" sx={{ mt: 4, mb: 4 }}>
      <Typography variant="h4" component="h1" gutterBottom align="center">
        Hệ thống giải phương trình bậc 2
      </Typography>
      
      {editingEquation ? (
        <Box sx={{ mb: 3 }}>
          <Typography variant="h5" gutterBottom>
            Sửa phương trình
          </Typography>
          <EquationForm 
            onSubmit={handleUpdateEquation} 
            initialValues={{ a: editingEquation.a, b: editingEquation.b, c: editingEquation.c }}
            isEditing={true}
          />
          <Box sx={{ mt: 2 }}>
            <Typography 
              variant="body2" 
              color="primary" 
              sx={{ cursor: 'pointer', textDecoration: 'underline' }}
              onClick={() => setEditingEquation(null)}
            >
              Hủy chỉnh sửa
            </Typography>
          </Box>
        </Box>
      ) : (
        <EquationForm onSubmit={handleAddEquation} />
      )}

      <EquationList 
        equations={equations} 
        onEdit={handleEditEquation} 
        onDelete={handleDeleteEquation} 
      />

      <Snackbar 
        open={!!notification} 
        autoHideDuration={6000} 
        onClose={handleCloseNotification}
        anchorOrigin={{ vertical: 'bottom', horizontal: 'center' }}
      >
        {notification ? (
          <Alert 
            onClose={handleCloseNotification} 
            severity={notification.type} 
            sx={{ width: '100%' }}
          >
            {notification.message}
          </Alert>
        ) : undefined}
      </Snackbar>
    </Container>
  );
}

export default App;
