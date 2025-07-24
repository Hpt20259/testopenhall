import React from 'react';
import { 
  Table, 
  TableBody, 
  TableCell, 
  TableContainer, 
  TableHead, 
  TableRow, 
  Paper, 
  IconButton, 
  Typography 
} from '@mui/material';
import { Edit as EditIcon, Delete as DeleteIcon } from '@mui/icons-material';
import { Equation } from '../types';

interface EquationListProps {
  equations: Equation[];
  onEdit: (equation: Equation) => void;
  onDelete: (id: number) => void;
}

const EquationList: React.FC<EquationListProps> = ({ equations, onEdit, onDelete }) => {
  if (equations.length === 0) {
    return (
      <Paper elevation={3} sx={{ p: 3, mt: 3 }}>
        <Typography variant="subtitle1" align="center">
          Chưa có phương trình nào được lưu.
        </Typography>
      </Paper>
    );
  }

  return (
    <TableContainer component={Paper} sx={{ mt: 3 }}>
      <Table>
        <TableHead>
          <TableRow>
            <TableCell>ID</TableCell>
            <TableCell>Hệ số a</TableCell>
            <TableCell>Hệ số b</TableCell>
            <TableCell>Hệ số c</TableCell>
            <TableCell>Kết quả</TableCell>
            <TableCell align="center">Thao tác</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {equations.map((equation) => (
            <TableRow key={equation.id}>
              <TableCell>{equation.id}</TableCell>
              <TableCell>{equation.a}</TableCell>
              <TableCell>{equation.b}</TableCell>
              <TableCell>{equation.c}</TableCell>
              <TableCell>{equation.result}</TableCell>
              <TableCell align="center">
                <IconButton 
                  color="primary" 
                  onClick={() => onEdit(equation)}
                  aria-label="Sửa"
                >
                  <EditIcon />
                </IconButton>
                <IconButton 
                  color="error" 
                  onClick={() => equation.id && onDelete(equation.id)}
                  aria-label="Xóa"
                >
                  <DeleteIcon />
                </IconButton>
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
};

export default EquationList;